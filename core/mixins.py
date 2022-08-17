class APIMixin(object):
    serializer_context = {}

    def get_serializer_context(self, **kwargs):
        """ Extra context provided to the serializer class. """
        socket_id = self.request.query_params.get('socket_id')
        serializer_context = super().get_serializer_context()
        serializer_context['current_user'] = self.request.user
        if socket_id:
            serializer_context['socket_id'] = socket_id
        for context_key, context_value in kwargs.items():
            serializer_context[context_key] = context_value
        return serializer_context

    def get_serializer(self, *args, **kwargs):
        """
        Return the serializer instance that should be used for validating and
        deserializing input, and for serializing output.
        """
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context(**self.serializer_context)
        return serializer_class(*args, **kwargs)
