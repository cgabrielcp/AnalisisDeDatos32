# Mi Proyecto

  ## Iniciar y conectar

  ```bash
  git init
  git remote add origin https://github.com/usuario/mi-proyecto.git

  Flujo diario

  git status
  git add .
  git commit -m "agrega función de login"
  git push origin main

  Trabajar con ramas

  git checkout -b feature/login
  # ...haces cambios...
  git add .
  git commit -m "login con email"
  git push origin feature/login

  Traer cambios del equipo

  git pull origin main