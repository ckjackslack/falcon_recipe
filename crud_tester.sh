echo "Getting all recipes:"
curl -s -X GET http://localhost:8000/recipes | python -m json.tool

echo
echo "Getting single recipe:"
curl -s -X GET http://localhost:8000/recipes/1 | python -m json.tool

echo
echo "Getting italian recipes:"
curl -s -X GET http://localhost:8000/recipes?category=italian | python -m json.tool

echo
echo "Posting new recipe:"
curl -s -i -X POST http://localhost:8000/recipes -H 'Content-Type: application/json' \
    -d '
        {
            "name": "Pierogi",
            "description": "boiled dumplings stuffed with savory or sweet fillings",
            "category": "russian"
        }
    '

echo
echo "Updating latest recipe:"
curl -s -i -X PUT http://localhost:8000/recipes/4 -H 'Content-Type: application/json' \
    -d '
        {
            "category": "polish"
        }
    '

echo
echo "Deleting latest recipe:"
curl -s -i -X DELETE http://localhost:8000/recipes/4