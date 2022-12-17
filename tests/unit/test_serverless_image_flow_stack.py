import aws_cdk as core
import aws_cdk.assertions as assertions

from serverless_image_flow.serverless_image_flow_stack import ServerlessImageFlowStack

# example tests. To run these tests, uncomment this file along with the example
# resource in serverless_image_flow/serverless_image_flow_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = ServerlessImageFlowStack(app, "serverless-image-flow")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
