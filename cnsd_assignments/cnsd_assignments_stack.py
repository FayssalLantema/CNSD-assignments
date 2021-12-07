from aws_cdk import (
    Stack,
    aws_ec2 as ec2, aws_ecs as ecs,
    aws_ecs_patterns as ecs_patterns)
)
from constructs import Construct



class CnsdAssignmentsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        vpc = ec2.Vpc(self, "3-1-2-vpc", max_azs=3)  # default is all AZs in region

        cluster = ecs.Cluster(self, "3-1-2-cluster", vpc=vpc)

        ecs_patterns.ApplicationLoadBalancedFargateService(self, "3-1-2-service",
                                                           cluster=cluster,  # Required
                                                           cpu=256,  # Default is 256
                                                           desired_count=1,  # Default is 1
                                                           task_image_options=ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                                                               image=ecs.ContainerImage.from_registry("nginx")),
                                                           memory_limit_mib=512,  # Default is 512
                                                           public_load_balancer=True)  # Default is False
