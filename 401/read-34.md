# API Deployment

## Reading
[Django Settings Best Practices](https://djangostars.com/blog/configuring-django-settings-best-practices/)
- Issues
    - different envs
    - sensitive data
    - sharing settings
    - settings are a Python code
- Different Approaches
    - settings_local.py
        - Pros
            - secrets not in VCS
        - Cons 
            - not in VCS (could lose some env settings)
            - python code - non-obvious logig
            - need settings_local.example (in VCS) to share default Django configs for devs
    - separate files for each env
        - extension of above approach
    - env variables
        use to solve issue with sensitive data
    - 12 Factors (recommendations by Heroku on how to build distributed web-apps that will be easy to deploy and scale in the Cloud)
        - codebase
        - dependencies
        - Config
        - Backing services
        - build, release, run
        - processes
        - port binding
        - concurrency
        - disposability
        - dev/prod parity
        - logs
        - admin processes

[SSH Tutorial](https://www.hostinger.com/tutorials/ssh-tutorial-how-does-ssh-work)
What is SSH?: Understanding Encryption, Ports and Connection
Download SSH cheat sheet [here](https://app.monstercampaigns.com/c/bt6ux7kak5s2ajnxx7km/).

Secure Shell Protocol

- remote admin protocol
- allows access, control, modify remote servers over the internet.
- created as a secure replacement for unencrypted Telnet
- Mac/Linux access from terminal
- Windows use SSH clients like 'Putty'
- linux
    - `ssh {user}@{host}`
        - user: account
        - host: IP address, server to access
        - client: computer used to access host
- Symmetrical Encryption
    - 'shared key'
- Asymmetrical encryption
    - public key and private key
- Hashing
    - HMACs
        - Hash-based Message Authentication Codes
        - each message must contain a MAC
- 

## Bookmark and Review
[White Noise](http://whitenoise.evans.io/en/stable/)
[Iaas](https://en.wikipedia.org/wiki/Infrastructure_as_a_service)
[PaaS](https://en.wikipedia.org/wiki/Platform_as_a_service)
[CORS](https://en.m.wikipedia.org/wiki/Cross-origin_resource_sharing)

## TIWKMA
- what are the pros/cons of hashing vs just symmetrical encryption in SSH auth