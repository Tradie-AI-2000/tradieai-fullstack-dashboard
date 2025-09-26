terraform {
  backend "gcs" {
    bucket = "tradieai-fullstack-production-terraform-state"
    prefix = "tradieai-fullstack-dashboard/prod"
  }
}
