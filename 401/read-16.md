# Serverless Functions

## Reading
[What is Serverless Computing?](https://www.ibm.com/cloud/learn/serverless)

- app dev / exec model
  - enables devs to build and run app code without provisioning or managing servers or backend infrastructure
  - lets devs focus on writing best front-end app code and biz-logic
  - only need to write app code and deploy to containers managed by a CSP
  - cloud handles routine infrastructure mgmt/maintenance (os updates/patches, security mgmt, capacity planning, system monitoring and more)
  - NO IDLE CAPACITY PAYMENTS
- not 'no servers'
  - just means cloud handles servers and devs don't see them
- AWS lambda, Azure Functions, Google Cloud Functions, IBM Cloud Code Engine
  - serverless computing, microservices and containers form a triumvirate of tech typically considered to be at the core of cloud-native applicaion development
- FaaS
  - enables devs to run code or containers in response toa  specific events or requests, without specifying or managin the infrastructure required to run to code.
- Serverless is more than FaaS
  - Serverless is an entire stack of services that can respond to events/requests, then scale to zero
    - databases/storage
      - SQL and NoSQL
        - serverless leans away from provisioning instances with defined capacity, connnection, and query limits
        - aims for models that scale linearly with demand (in infrastructure and pricing)
    - Event Streaming / messaging
      - serverless arch well suited for event-driven and stream-processing workloads (Apache Kafka)
    - API gateways
      - act as proxies to web actions
      - provide http method routing
      - client ID / secrets
      - rate limits
      - CORS 
      - viewing API usage
      - viewing response logs
      - API sharing policies

- Serverless vs. PaaS, containers, and VM's
  - Platform as a service, cont's, vm's, serverless all play important roles in cloud app dev & compute ecosystem
    - provisioning time
      - measurdin ms for serverless, minutes-hours for other models
    - Admin burden
      - none for serverless, light-med-heavy for PaaS, containers, vm's (respectively)
    - Scaling
      - serverless
        - auto-scaling (including scaling to zero)
      - others
        - slow scaling, careful tuning requried of auto-scaling rules, NO scaling to zero
    - capacity planning
      - SL none required
      - others: some auto-scalability some cap plan
    - statelessness
      - SL inherent (scalability never a problem, handled by external service/resource)
      - other: PaaS, cont's, vm's leverage http, keep open socket or connection for long periods of time, store state in memory between calls
    - HA / DR
      - high availability / disaster recovery
        - inherent in serverless
          - no extra effort/cost
        - others: aditional cost/mgmt effort
          - vm's / containers: infrastructure can be restarted automatically
    - resource utilization
      - SL 100% efficient, no idle cap
      - others: some degree of idle utilization
    - billing granularity
      - SL metered in units of 100ms
      - others: hour or minute
- Serverless, Kubernetes and Knative
  - Kubernetes
    - open-source container orchestration platform that automates the deployment, management, and scaling of containers.
    - automation dramatically simplifies the development of container-based apps
    - Serverless apps often deployed in containers
      - solo, kubernetes can't run serverless apps without special sofware that integrates kubernetes with specific cloud provider's serverless platform
      - Knative provides serverless framework for kubernetes
        - open-source extension to kubernetes 
          - enables any container to run as a serverless workload on any cloud platform that runs kubernetes
        - works by abstracting away the code and handling network routing, event triggers, and autoscaling for serverless execution.
        - transparent to developers--devs just build a container as usual using kubernetes and knative does the rest, runnin the container as a serverless workload.
- Pros/Cons
  - Pros
    - improved dev productivity
      - allows focus on writing code, not managing infrastructure
        - gives devs more time to innovate and optimize front-end app functionality/biz logic
    - pay for execution only
      - scale-to-zero
        - vs IaaS compute model: customers pay for physical servers, vms, and other resources until decomissioned
    - develop in any language
      - polyglot env
    - streamlined dev/devops cycles
      - no need define infrastructure required to integrate, test, deliver, deploy code
        - all built in
    - const effective performance
      - faster/more cost-effective than some workoads
    - usage viz
      - near-total viz into system and user times
      - can aggregate usage info sytematically
  - Cons
    - unacceptable latency for certain apps
      - sometimes need to start from zero to serve new request after scaling to zero
        - may sometimes be unacceptable (trading)
    - higher costs for stable/predictable workloads
      - cheaper for spiky workloads, not for predictable, steady or long-running processes
    - monitoring and debugging issues
      - SL
        - exacerbates issue complexity
        - difficult or impossible to monitor or debug serverless functions using existing tools/processes
    - vendor lock-in
      - migrating to a new cloud provider could be challenging
      - not portable like VM's, or docker containers
      - may have to rewrite platform across providers
## Video
[What is Serverless?](https://www.youtube.com/watch?v=vxJobGtqKVM)

- Not responsible for mgmt/provisioning 
- deployment model evolution over time
- Cloud takes over more and more config/os/patching
- BM, VM, Containers, Serverless

- Pay for execution
- Auto Scalable
- Faster time to market FTM
- Polyglot
- Highly available
  - cloud providor takes care of mzr's
  - other services available
- No idle time in Serverless, charged by functionality

## Additional Resources
[venv - Creation of Virtual Environments](https://docs.python.org/3/library/venv.html)

[Vercel - Get Started](https://vercel.com/docs/get-started)

[http.server](https://pymotw.com/3/http.server/index.html)

[Requests](https://docs.python-requests.io/en/latest/)

[Python & API's](https://realpython.com/python-api/)

## Bookmark for Review
[Serverless Functions](https://vercel.com/docs/concepts/functions/serverless-functions)

[Effective Python Environment](https://realpython.com/effective-python-environment/)
## Things I want to know more about

- looking forward to getting into cloud computing, containers, and what makes them tick
- what is at the base of serverless? ML? AI?