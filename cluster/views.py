from django.shortcuts import render
from .models import Cluster
from django.utils import timezone
from .forms import ClusterForm

# Create your views here.
def addcluster(request):
    
    
    if(request.method == "POST"):
        form = ClusterForm(request.POST, request.FILES)
    else:
        form = ClusterForm()
        return render(request, 'cluster.html', {'form': form})
    
        
        # cluster = Cluster()
        # cluster.cluster_name = request.POST['clustername']
        # cluster.cluster_type = request.POST['typeradio']
        # cluster.bearer_token = request.POST['bearertoken']
        # cluster.kubeconfig = request.FILES.get('kubecfg')

    #     # cluster.save()
    
    # return render(request, 'addcluster.html')