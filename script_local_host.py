#!/bin/bash

# Fonction pour pousser un projet vers GitHub
push_project() {
  local project_path=$1
  local repo_url=$2

  cd "$project_path" || exit
  git init
  git add .
  git commit -m "Initial commit with necessary files"
  git remote add origin "$repo_url"
  git pull origin main --allow-unrelated-histories
  git push -u origin main
}

# Pousser les différents projets
push_project "/Users/gau20/Desktop/stage programmation/N-back HDG/condition 3/n1-back" "https://github.com/G2A0U/C3N1BACK.git"
push_project "/Users/gau20/Desktop/stage programmation/N-back HDG/condition 3/n2-back" "https://github.com/G2A0U/C3N2BACK.git"
push_project "/Users/gau20/Desktop/stage programmation/N-back HDG/condition 3/n3-back" "https://github.com/G2A0U/C3N3BACK.git"

echo "All projects pushed successfully."
