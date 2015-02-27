
DESCRIPTION OF THE URLS API
_______________________________

# TODO: this file is temporal

Api base, has only temporarily managing for users

    STEPS #6.1 CALLING ALL USERS -- METHOD GET

        Following urls:

        http://localhost/api/users/


    STEPS #6.1 CALL A USER BY ID -- METHOD GET

        Following urls:

        http://localhost/api/users/id/

=========================================================================

STEPS #7 DIFFERENCES BETWEEN THE URLS


This step is just to show the difference between urls, and differences in functionality



    STEPS #7.1 URLS http://localhost/api/usuarios/ o URLS http://localhost/api/usuarios/id/

        Only get a view of the users that exist in the database . Also search by user ID,
        but you can not delete or update



    STEPS #7.1 URLS http://localhost/api/users/ o URLS http://localhost/api/users/id/

        This url, will be able to search, modify and delete user information

MORE URLS
    -------------
    POST http://localhost/api/token/ -d '{username:"usuario", password:"12345"}'
    GET http://localhost/api/token/user/
    -------------
    GET     http://localhost/api/users/
    GET     http://localhost/api/users/{pk}/
    POST    http://localhost/api/users/{pk}/
    PUT     http://localhost/api/users/{pk}/
    PATCH   http://localhost/api/users/{pk}/
    DELETE  http://localhost/api/users/{pk}/
    -------------
    GET     http://localhost/api/foodgroup/
    GET     http://localhost/api/foodgroup/{pk}/
    POST    http://localhost/api/foodgroup/{pk}/
    PUT     http://localhost/api/foodgroup/{pk}/
    PATCH   http://localhost/api/foodgroup/{pk}/
    DELETE  http://localhost/api/foodgroup/{pk}/
    -------------
    GET     http://localhost/api/foods/
    GET     http://localhost/api/foods/{pk}/
    POST    http://localhost/api/foods/{pk}/
    PUT     http://localhost/api/foods/{pk}/
    PATCH   http://localhost/api/foods/{pk}/
    DELETE  http://localhost/api/foods/{pk}/

