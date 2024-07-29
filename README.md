# Blog API Project

This project is a CRUD blog website built using Django Rest Framework (DRF). It provides a set of endpoints to manage blog articles, including creating, reading, updating, and deleting articles.

## Features

- Return a list of articles with publication date and tags
- Retrieve a single article by its ID
- Create a new article
- Delete a single article
- Update a single article

## Endpoints

1. **List Articles**  
   `GET /api/articles/`  
   Returns a list of articles including their publication date and tags.

2. **Retrieve Single Article**  
   `GET /api/blogposts/<id>/`  
   Returns a single article specified by its ID.

3. **Create Article**  
   `POST /api/blogposts/`  
   Creates a new article. Requires article data in the request body.

4. **Delete Article**  
   `DELETE /api/blogposts/<id>/`  
   Deletes the specified article by its ID.

5. **Update Article**  
   `PUT /api/blogposts/<id>/`  
   Updates the specified article by its ID. Requires updated article data in the request body.

