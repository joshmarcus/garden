# EC2 canary readiness — operator preparation

Read-only inspection at2026-09-07 18:28Z. No cloud resources were created.

Scoped garden-provisioner authentication succeeds as ContextGardenProvisioner in account350111791226. Explicit us-east-1 inventory with ManagedBy=context-garden and Pool=phase05 found zero subnets, security groups and instances. Do not use the root default profile. CG345 implementation afadab351a024cad3bfd8bcb9cc54b36ee61c416 passes CI34149530112 but has not passed automated review or a live canary.

## Disabled proposal

One on-demand host maximum, zero idle/minimum hosts, desired0 and enabledfalse. Select one of the existing allowed t3.xlarge/m7i.xlarge types only after obtaining current pricing; no Spot until ordinary enrollment/retirement works. Proposed execution window30minutes with a separately approved all-in spend bound before enabling. No NAT gateway, load balancer, public ingress or persistent dev disk in this first worker experiment. Pin an allowed Canonical Ubuntu AMI, reviewed bootstrap version and exact worker package build; encrypted root volume, IMDSv2 and owner/pool tags remain mandatory. Terminate in finally and inventory instances, volumes and public IPs afterward. Estimates are not a provider billing cap; an independent deadline/cleanup check is required.

## Prerequisites, not worker implementation revisions

- Provisioner role exists, but preapproved tagged subnet/security group do not. The role is deliberately not a general networking/IAM administrator. Prepare an exact network/resource proposal through an authorized administrative identity; do not broaden or fall back to root automatically.
- ContextGardenWorker instance profile and minimal enrollment-secret access need verified provisioning. Store only secret references in configuration; no operator/harness credentials in user data or briefs.
- Current endpoint is tailnet-only https://babel.taild4d2ae.ts.net. A plain EC2 host cannot be assumed to reach it. Design scoped tailnet enrollment or another approved private route before opening any public exposure. Do not enable Funnel.
- CG216 remote protocol is not yet approved/deployed. Verify actual served HTTP registration/claim/heartbeat/finish before treating an EC2 host as a registered usable worker. Current CG345 evidence does not prove this.
- Supply a current hourly estimate and a concrete reviewed all-in budget/enable decision only once the network, profile, endpoint, image and exact reviewed build are resolved.

Preserve CG345 completed code. Its waiting-human card asks for operator preparation, not new access keys from Josh. Keep live-canary criterion unproven; do not blindly resume a model run without the prerequisites. CG346 integration and CG347 interruption recovery remain separate work.
