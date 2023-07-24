import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as lambda from 'aws-cdk-lib/aws-lambda'
import * as dotenv from 'dotenv';
import * as apiGateway from 'aws-cdk-lib/aws-apigateway'
import { Lambda } from 'aws-cdk-lib/aws-ses-actions';

// import * as sqs from 'aws-cdk-lib/aws-sqs';

dotenv.config()

export class CopykittInfraStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);
   
   const layer = new lambda.LayerVersion(this, "BaseLayer", {
    code: lambda.Code.fromAsset("lambda_base_layer/layer.zip"),
    compatibleRuntimes: [lambda.Runtime.PYTHON_3_9]
   })

   const apiLambda = new lambda.Function(this, "ApiFunction", {
    runtime: lambda.Runtime.PYTHON_3_9,
    code: lambda.Code.fromAsset("../app/"),
    handler: "copykitt_api.handler",
    layers: [layer],
    environment: {
      OPENAI_API_KEY: process.env.OPENAI_API_KEY ?? "",
    }
   })
   const copyKittApi = new apiGateway.RestApi(this, "RestApi", {
    restApiName: "CopyKitt Api",
   })

   const lambdaApiIntegration = new apiGateway.LambdaIntegration(apiLambda);
   copyKittApi.root.addProxy({
    defaultIntegration: lambdaApiIntegration,
   })
  }
}