from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from utils.argocd_api import get_request_with_bearer, get_argocd_token, create_argocd_cluster
from utils.kubernetes_api import parsing_kube_confing
from django.conf import settings
from .models import Cluster


ARGOCD_URL = getattr(settings, 'ARGOCD_URL', None)
ARGOCD_USERNAME = getattr(settings, 'ARGOCD_USERNAME', None)
ARGO_PASSWORD = getattr(settings, 'ARGO_PASSWORD', None)

# Create your views here.
@login_required
def addcluster(request):
    if(request.method == "POST"):
        cluster = Cluster()
        cluster.cluster_name = request.POST['clustername']
        cluster.cluster_type = request.POST['typeradio']
        cluster.bearer_token = request.POST['bearertoken']
        cluster.kubeconfig = request.FILES.get('kubecfg')
        # check file
        file_content = request.FILES['kubecfg'].read().decode('utf-8')
        cluster_url, cluster_ca = parsing_kube_confing(file_content)
        print(cluster_url, cluster_ca)
        if cluster_url == "-1" or cluster_ca == "-1":
            print("kubernetes config 파일이 아닙니다")
            return render(request, 'addcluster.html')
        resp = get_request_with_bearer(cluster_url, cluster.bearer_token)
        if resp.status_code == 200:
            print("서버 접속이 가능합니다.")
        else:
            print("파일 또는 토큰 확인 필요")
            print("error 종료")
        cluster.cluster_url = cluster_url
        user_id = request.user
        # get argocd_token
        resp = get_argocd_token(ARGOCD_URL, ARGOCD_USERNAME, ARGO_PASSWORD)
        argo_bearer_token=''
        # 토큰 발급 실패면, 에러 팝업
        if resp.status_code == 200:
            print("토큰 발급 성공")
            argo_bearer_token = resp.json()['token']
            print(argo_bearer_token)
        else:
            print("토큰 발급 실패")

        # 클러스터 생성 요청
        resp = create_argocd_cluster(ARGOCD_URL, argo_bearer_token, cluster_url, cluster.cluster_name, cluster.bearer_token,
                                     cluster_ca)
        if resp.status_code == 200:
            print("서버 생성 성공 ")
            print(resp.text)
        else:
            print("서버 생성 실패 ")




        # cluster.save()
    
    return render(request, 'addcluster.html')

# # Create your views here.
# def addcluster(request):
#     if request.method == "POST":
#         form = ClusterForm(request.POST, request.FILES)
#         print(request.FILES)
#         if form.is_valid():
#             cluster = form.save(commit=False)
#             cluster.save()
#             return redirect("/")
#     else:
#         form = ClusterForm()
    
#     return render(request, 'cluster.html', {'form': form})