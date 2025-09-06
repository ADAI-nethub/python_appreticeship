from rest_framework.permissions import IsAuthenticated

class StoryCreateAPI(generics.CreateAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Link story to logged-in artisan
        serializer.save(artisan=self.request.user.artisan)