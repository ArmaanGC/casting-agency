#!/bin/bash
export DATABASE_URL="postgres://pdwptvgutkzryv:9412ade8f0b38973cf7d7d1219e9673d588c89e0f92eac3a5a1ae81eaefa2a9f@ec2-54-236-156-167.compute-1.amazonaws.com:5432/d6hmdtl72hg1j"
export EXCITED="true"

# Auth0 config
export AUTH0_DOMAIN='dev-jdd6v-si.us.auth0.com'
export ALGORITHMS=['RS256']
export API_AUDIENCE='castingagency'

# Tokens
export CASTING_ASSISTANT='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlVScURuVWxJWlFYQko5MWFOVkdWOCJ9.eyJpc3MiOiJodHRwczovL2Rldi1qZGQ2di1zaS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjFkMTgwYzBlMDljODMwMDZmMWIyMjQ2IiwiYXVkIjoiY2FzdGluZ2FnZW5jeSIsImlhdCI6MTY0MTMwNjY1MCwiZXhwIjoxNjQxMzEzODUwLCJhenAiOiJ6OW40SUF6OWZYNEkwUVljS2RnSXpBdnVaaEpoVzF0eSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.OdaUtM4Hbn6_TEUlh7TgPWGQtO-V9OOPdzrg2HNrcF08Q_w8r9Nz4M1GuuBPNMuGqf3bF8_LG8fXaKRrO9VZhD3pHs3kXI7-K8FPv6zsZbj7ZcvfbloNWYlm2WWiFlpQ-wZMrgw0myLom4P3cvxGntwVU5wWdr5oA9HXGvcgdSF4JA6wX_OWJqQhYHZV__Xc1ZUjV1o8aYxPfFa2p_0MJhgILpogcPurewTClYcOyk_49tsnbv4YGLkyH2ovuCyB3Lmj9oHlgN32OCXHX1DIjwIEffp3GYIiL9h-TMYMEvoO9HwhxWCwEK9A3QP6alTv8dGqtAJUQqmYzmFwycnJkA'
export CASTING_DIRECTOR='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlVScURuVWxJWlFYQko5MWFOVkdWOCJ9.eyJpc3MiOiJodHRwczovL2Rldi1qZGQ2di1zaS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjFkMTgwOTRmYTJjZDEwMDY5ZWU2Mjc5IiwiYXVkIjoiY2FzdGluZ2FnZW5jeSIsImlhdCI6MTY0MTMwNjY0MywiZXhwIjoxNjQxMzEzODQzLCJhenAiOiJ6OW40SUF6OWZYNEkwUVljS2RnSXpBdnVaaEpoVzF0eSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicG9zdDphY3RvcnMiLCJ1cGRhdGU6YWN0b3JzIiwidXBkYXRlOm1vdmllcyJdfQ.uIBsOzRMv0a3DrEBkNssHk0uZ1QZNzwIyDDUGYxZ-hNlOswcx09VlyABQxsj4aao6kfZBnHCZrQpqGiygPH3l0knbP-Bu2DqEGZN76bSb9z7De35iMv5JI7NuAgUEgd3SaSTI7J-QLlMg9OAOC0gqZc4NkVGx91OtA_c1SlWN7EYY6kLiNtOEPZXFR5C3U8hWIrVum3xcZU5_WVBM5IjwswuodWChIgE2C-1B1eXzMWmRfISnnmwx7hTJAWNqQ1lrvH0ewycMxE6A3VsUntgFCKXWN1OuedJ-EVy1hICSjOAClyUuWrJjqVwTLoyrVwYx8xBI_IVjfIhXxfPEsBHSw'
export EXECUTIVE_PRODUCER='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlVScURuVWxJWlFYQko5MWFOVkdWOCJ9.eyJpc3MiOiJodHRwczovL2Rldi1qZGQ2di1zaS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjFkMTgwNWZmYTJjZDEwMDY5ZWU2MjZlIiwiYXVkIjoiY2FzdGluZ2FnZW5jeSIsImlhdCI6MTY0MTMwNjYzOCwiZXhwIjoxNjQxMzEzODM4LCJhenAiOiJ6OW40SUF6OWZYNEkwUVljS2RnSXpBdnVaaEpoVzF0eSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiLCJ1cGRhdGU6YWN0b3JzIiwidXBkYXRlOm1vdmllcyJdfQ.PMPj3xR9N_XiQ4udbRdxSLIljrsgvPWvhvGIbxLXmqSTqwpmFKEw5lbVtIieVmMFq37jN38-HOfRsGV9LVcsI2_SLGJZqCo7xrA451EkdUK2cXJ-a2BxUGQCo7VMsZSmK0dGR6JL_mT1YUjyGj1TOLW-64zPsGj-TXD9OEn1gpWE62K1rTnX4DImdv02t8IVBV8OUrtYdIcvVVqiTKxzFl_IqS60D2MFEgLvqBjJr-gKURCrziEm-HTNLDIbtCdgnotFrKD7X2ZDgFrC2_YVQ-BGe5HUyG7_1X5y0n8B-hcovT8Zj-CydluLapUOeFa3DMKswk86ZAICSSuUnW0BCQ'

echo "setup.sh script executed successfully!"