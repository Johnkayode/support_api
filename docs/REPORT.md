# API Endpoints Report

## Summary

This report documents the identification and resolution of issues in the provided API endpoints. 

## Issues Found

1. **Lack of Exception Handling in the `GET` Method:**
   - The `GET` method did not handle the case where the requested `Item` with the specified `item_id` did not exist.

2. **Redundant Return Statement in the `POST` Method:**
   - A redundant `return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)` statement was present after `return Response(status=status.HTTP_201_CREATED)` in the `POST` method.

3. **Missing Validation in the `POST` Method:**
   - The `POST` method did not validate the serializer data before attempting to save the data.

4. **Internal Server Error:**
   - A 500 error is returned when a `GET` request is made without passing the `id` path parameter.

## Fixes

The following fixes were made to address the identified issues:

1. Introduced the use of DRF's `GenericViewSets` and `Mixins`. This fixes all isses above as it handles basic CRUD actions. [Read](https://www.django-rest-framework.org/api-guide/viewsets/)

2. The 500 error is handled by returning a `405 Method Not Allowed` error instead.

## Unit Tests

Unit tests were implemented to validate the changes. The tests were designed using Django's testing framework.

- `test_retrieve_existing_item`: Checks if a valid `Item` object is retrieved successfully.
- `test_retrieve_without_item_id`: Verifies that attempting to make a `GET` request without the id parameter returns a 405 method_not_allowed response.
- `test_retrieve_nonexistent_item`: Verifies that attempting to retrieve a nonexistent item returns a 404 response.
- `test_create_valid_item`: Ensures that a valid item can be successfully created.
- `test_create_invalid_item`: Checks that attempting to create an item with missing data returns a 400 response.

## Conclusion

The identified issues have been addressed, and the changes have been validated through comprehensive unit tests. 
