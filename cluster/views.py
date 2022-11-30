from django.shortcuts import render, redirect
from .models import Cluster
from django.utils import timezone
from .forms import ClusterForm

# Create your views here.
def addcluster(request):
    if(request.method == "POST"):
        cluster = Cluster()
        cluster.cluster_name = request.POST['clustername']
        cluster.cluster_type = request.POST['typeradio']
        cluster.bearer_token = request.POST['bearertoken']
        cluster.kubeconfig = request.FILES.get('kubecfg')
        print(cluster.kubeconfig)
        cluster.save()
    
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