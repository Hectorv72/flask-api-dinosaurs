from app import app
import project.routes.carnivores

if __name__ == '__main__':
  # run app in debug mode on port 5000
  app.run(debug=True, port=5000)