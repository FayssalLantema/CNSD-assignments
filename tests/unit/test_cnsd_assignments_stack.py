import aws_cdk as core
import aws_cdk.assertions as assertions

from cnsd_assignments.cnsd_assignments_stack import CnsdAssignmentsStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cnsd_assignments/cnsd_assignments_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CnsdAssignmentsStack(app, "cnsd-assignments")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
