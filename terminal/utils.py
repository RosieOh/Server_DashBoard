import boto3
import os
from dotenv import load_dotenv

load_dotenv()

print("AWS_ACCESS_KEY_ID:", os.getenv('AWS_ACCESS_KEY_ID'))
print("AWS_SECRET_ACCESS_KEY:", os.getenv('AWS_SECRET_ACCESS_KEY'))
print("AWS_REGION:", os.getenv('AWS_REGION'))

# EC2 클라이언트 생성
ec2 = boto3.client(
    'ec2',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name=os.getenv('AWS_REGION')
)

# EC2 인스턴스 상태 조회
def describe_instances():
    response = ec2.describe_instances()
    print(response)  # 추가: 반환되는 응답 확인
    return response['Reservations']

# EC2 인스턴스 시작
def start_instance(instance_id):
    ec2.start_instances(InstanceIds=[instance_id])

# EC2 인스턴스 종료
def stop_instance(instance_id):
    ec2.stop_instances(InstanceIds=[instance_id])
