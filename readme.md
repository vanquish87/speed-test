FastAPI:

"/benchmark_user_model_serializer/" ~ 32 ms

"/benchmark_user_read_only_model_serializer/" ~ 31 ms

"/benchmark_user_serializer/" ~ 30 ms


DRF:

"run_benchmark/" ~ 5 ms

"benchmark_user_model_serializer/" ~ 2100 ms

"benchmark_user_read_only_model_serializer/" ~ 2300 ms

"benchmark_user_serializer/" ~ 580 ms




Conclusion:

FastAPI significantly outperforms Django REST framework (DRF) in terms of serialization speed for user data.
