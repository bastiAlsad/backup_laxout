from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from urllib.parse import unquote
from laxout_app import models
from . import serializers
from django.utils import timezone
from datetime import date


@api_view(["POST"])
def autorise_laxout_user(request):
    user_uid = request.data["user_uid"]
    try:
        user = models.LaxoutUser.objects.get(user_uid=user_uid)
    except models.LaxoutUser.DoesNotExist:
        return Response({"details": "user not found"})

    physio_instance = user.created_by

    if not isinstance(physio_instance, User):
        return Response({"details": "physio not found for the given user"})

    token, created = Token.objects.get_or_create(user=physio_instance)
    return Response({"token": token.key})


@api_view(["GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_username(request):
    user_id = request.headers.get("user_uid")
    decoded_user_uid = unquote(user_id)
    if user_id is None:
        print("kakakakkakakkaka")
    print(user_id)
    print(decoded_user_uid)
    laxout_user_instance = models.LaxoutUser.objects.get(user_uid=decoded_user_uid)
    if laxout_user_instance is None:
        return Response({"method": "forbidden"})
    return Response("Es war{}".format(laxout_user_instance.laxout_user_name))


@api_view(["GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_exercises(request):
    user_id = request.headers.get("user_uid")
    if user_id is None:
        return Response(status=status.HTTP_403_FORBIDDEN)
    decoded_user_uid = unquote(user_id)
    user_instance = models.LaxoutUser.objects.get(user_uid=decoded_user_uid)
    if user_instance is None:
        return Response(status=status.HTTP_403_FORBIDDEN)
    exercises = user_instance.exercises.all()
    serializer = serializers.LaxoutExerciseSerializer(exercises, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_laxcoins_amount(request):
    user_uid = request.headers.get("user_uid")
    if user_uid == None:
        return Response(status=status.HTTP_403_FORBIDDEN)
    decoded_user_uid = unquote(user_uid)
    user_instance = models.LaxoutUser.objects.get(user_uid=decoded_user_uid)
    laxcoins_amount = user_instance.laxout_credits
    return Response({"laxcoins_amount": str(laxcoins_amount)})


@api_view(["POST"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def post_leistungs_index(request):
    user_uid = request.headers.get("user_uid")
    if user_uid == None:
        return Response(status=status.HTTP_403_FORBIDDEN)
    user_instance = models.LaxoutUser.objects.get(user_uid=user_uid)
    if user_instance == None:
        return Response(status=status.HTTP_403_FORBIDDEN)
    index = request.data["index"]
    if index == None:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    index_instance = models.IndexesLaxoutUser.objects.create(
        index=index, created_by=user_instance.id
    )
    if user_instance.last_login.date() != date.today():
        user_instance.indexes.add(index_instance)
        user_instance_coins = user_instance.laxout_credits
        user_instance_coins += 100
        user_instance.laxout_credits = user_instance_coins
        user_instance.last_login = date.today()
        user_instance.save()
    
    return Response(status=status.HTTP_200_OK)


@api_view(["POST"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def post_pain_level(request):
    user_uid = request.headers.get("user_uid")
    decoded_user_uid = unquote(user_uid)
    user_instance = models.LaxoutUser.objects.get(user_uid=decoded_user_uid)
    if user_instance == None:
        return Response(status=status.HTTP_403_FORBIDDEN)
    physio = user_instance.created_by
    pain_level = request.data["pain_level"]
    if pain_level == None:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    physio_instance = models.UserProfile.objects.get(user=physio)
    pains_instance = models.Pains.objects.create(paint_amount=pain_level)
    physio_instance.average_pain.add(pains_instance)
    return Response(status=status.HTTP_200_OK)

#################################Coupon Logic######################################

@api_view(["GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_coupons(request):
    user_uid = request.headers.get("user_uid")
    if user_uid == None:
        return Response(status=status.HTTP_403_FORBIDDEN)
    decoded_user_uid = unquote(user_uid)
    user_instance = models.LaxoutUser.objects.get(user_uid=decoded_user_uid)
    if user_instance == None:
        return Response(status=status.HTTP_403_FORBIDDEN)
    coupons = models.Coupon.objects.all()
    if coupons == None:
        return Response(status=status.HTTP_204_NO_CONTENT)
    serializer = serializers.CouponSerializer(coupons, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_coupons_for_user(request):
    user_uid = unquote(request.headers.get('user_uid'))
    if user_uid == None:
        return Response(status= status.HTTP_403_FORBIDDEN)
    user_instance = models.LaxoutUser.objects.get(user_uid= user_uid)
    if user_instance == None:
        return Response(status= status.HTTP_403_FORBIDDEN)
    coupons = user_instance.coupons.all()
    print("data sended getcouponuser")
    serializer = serializers.CouponSerializer(coupons, many = True)
    return Response(serializer.data, status= status.HTTP_200_OK)
    

@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def buy_coupon(request):
    user_uid = unquote(request.headers.get('user_uid'))
    if user_uid == None:
        return Response(status= status.HTTP_403_FORBIDDEN)
    coupon_id = request.data['coupon_id']
    coupon_instance = models.Coupon.objects.get(id = coupon_id)
    if coupon_instance == None:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    user_instance = models.LaxoutUser.objects.get(user_uid= user_uid)
    old_coins_amount = user_instance.laxout_credits
    if old_coins_amount > coupon_instance.coupon_price:
        print("sack")
        print(coupon_instance.coupon_price)
        print("This is the old amount {}".format(user_instance.laxout_credits))
        print("This is the coupon price {}".format(coupon_instance.coupon_price))
        old_coins_amount -= coupon_instance.coupon_price
        print("This is the new amount {}".format(old_coins_amount))
        user_instance.laxout_credits = old_coins_amount
        user_instance.coupons.add(coupon_instance)
        user_instance.save()
        return Response({'rabatCode': coupon_instance.rabbat_code},status=status.HTTP_200_OK)
    return Response({'details': "not enough coins"}, status= status.HTTP_406_NOT_ACCEPTABLE)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_coupon_user(request):
    user_uid = unquote(request.headers.get('user_uid'))
    if user_uid == None:
        return Response(status= status.HTTP_403_FORBIDDEN)
    coupon_id = request.data['coupon_id']
    coupon_instance = models.Coupon.objects.get(id = coupon_id)
    if coupon_instance == None:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    user_instance = models.LaxoutUser.objects.get(user_uid= user_uid)
    to_delete = user_instance.coupons.get(id = coupon_id)
    user_instance.coupons.remove(to_delete)
    user_instance.save()
    return Response(status=status.HTTP_200_OK)



#################################Coupon Logic######################################





#complete exercise for user
@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def finish_exercise(request):
    user_uid = unquote(request.headers.get('user_uid'))
    if user_uid == None:
        return Response(status= status.HTTP_403_FORBIDDEN)
    user_instance = models.LaxoutUser.objects.get(user_uid = user_uid)
    if user_instance == None:
        return Response(status= status.HTTP_403_FORBIDDEN)
    exercise_id = request.data['exercise_id']
    if exercise_id == None:
        return Response(status= status.HTTP_500_INTERNAL_SERVER_ERROR)
    models.DoneExercises.objects.create(exercise_id= exercise_id, laxout_user_id= user_instance.id)
    return Response(status=status.HTTP_201_CREATED)




@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def skip_exercise(request):
    user_uid = unquote(request.headers.get('user_uid'))
    if user_uid == None:
        return Response(status= status.HTTP_403_FORBIDDEN)
    user_instance = models.LaxoutUser.objects.get(user_uid = user_uid)
    if user_instance == None:
        return Response(status= status.HTTP_403_FORBIDDEN)
    exercise_id = request.data['exercise_id']
    if exercise_id == None:
        return Response(status= status.HTTP_500_INTERNAL_SERVER_ERROR)
    models.SkippedExercises.objects.create(skipped_exercise_id= exercise_id, laxout_user_id= user_instance.id)
    return Response(status=status.HTTP_200_OK)
    

@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def finish_workout(request):
    user_uid = unquote(request.headers.get('user_uid'))
    if user_uid == None:
        return Response(status= status.HTTP_403_FORBIDDEN)
    user_instance = models.LaxoutUser.objects.get(user_uid = user_uid)
    if user_instance == None:
        return Response(status= status.HTTP_403_FORBIDDEN)
    workout_id = request.data['workout_id']
    if workout_id == None:
        return Response(status= status.HTTP_500_INTERNAL_SERVER_ERROR)
    models.DoneWorkouts.objects.create(workout_id = workout_id, laxout_user_id = user_instance.id)
    if user_instance.last_login_2.date() != date.today():
        user_instance_coins = user_instance.laxout_credits
        user_instance_coins += 100
        user_instance.laxout_credits = user_instance_coins
        user_instance.last_login_2 = date.today()
        user_instance.save()
    return Response(status=status.HTTP_201_CREATED)







#note a skipped exercise