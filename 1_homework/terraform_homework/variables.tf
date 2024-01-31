variable "credentials" {
  description = "My credentials"
  default     = "./keys/my_creds.json"
}

variable "project" {
  description = "Project"
  default     = "de-course-2024-412715"
}

variable "region" {
  description = "Project region"
  default     = "us-central1"
}

variable "location" {
  description = "Project Location"
  default     = "US"
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  default     = "de_course_demo_dataset"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  default     = "de-course-2024-412715-terraform-bucket"
}

variable "gsc_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDART"
}
