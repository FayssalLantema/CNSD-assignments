from aws_cdk import (
    Stack,
    aws_ec2 as ec2, aws_ecs as ecs,
    aws_ecs_patterns as ecs_patterns
)
from constructs import Construct


class CnsdAssignmentsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        vpc = ec2.Vpc(self, "Assignment312Vpc", max_azs=3)  # default is all AZs in region

        cluster = ecs.Cluster(self, "Assignment312Cluster", vpc=vpc)

        ecs_patterns.ApplicationLoadBalancedFargateService(self, "Assignment312Service",
                                                           cluster=cluster,  # Required
                                                           task_image_options=ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                                                               image=ecs.ContainerImage.from_registry("nginx")),
                                                           desired_count=1,
                                                           public_load_balancer=True)  # Default is False
