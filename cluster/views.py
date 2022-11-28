from django.shortcuts import render
from .models import Cluster
from django.utils import timezone

# Create your views here.
def addcluster(request):
    print("hello")
    if(request.method == "POST"):
        cluster = Cluster()
        cluster.cluster_name = request.POST['clustername']
        cluster.cluster_type = request.POST['typeradio']
        cluster.bearer_token = request.POST['bearertoken']
        cluster.kubeconfig = request.FILES.get('kubecfg')

        cluster.save()
    
    return render(request, 'addcluster.html')