from django.shortcuts import render
from django.http import HttpResponse
from .utils import describe_instances, start_instance, stop_instance

# EC2 인스턴스 대시보드
def ec2_dashboard(request):
    instances = describe_instances()  # EC2 인스턴스 상태 조회
    print(instances)  # 추가: 템플릿으로 넘겨지는 instances 값 확인
    return render(request, 'terminal/ec2_dashboard.html', {'instances': instances})

# EC2 인스턴스 시작
def start_instance_view(request, instance_id):
    start_instance(instance_id)  # EC2 인스턴스 시작
    return HttpResponse(f"Instance {instance_id} started.")

# EC2 인스턴스 종료
def stop_instance_view(request, instance_id):
    stop_instance(instance_id)  # EC2 인스턴스 종료
    return HttpResponse(f"Instance {instance_id} stopped.")

def main_page(request):
    return render(request, 'main.html')
