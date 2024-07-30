from ..Services.login_service import UserService, LoginService
from ..Services.user_service import UserListService, UserCreateService, UserUpdateService, UserDeleteService, UserDetailsService, UserPostsService
from ..Services.post_service import PostListService, PostCreateService, PostUpdateService, PostDeleteService
from ..Services.story_service import StoryListService, StoryCreateService, StoryUpdateService, StoryDeleteService
from ..Services.friend_request_service import FriendRequestListService, FriendRequestCreateService, FriendRequestUpdateService, FriendRequestDeleteService
from ..Services.amigos_service import AmigosListService, AmigosCreateService, AmigosDeleteService
from ..Services.message_service import MessageListService,MessageDetailService, MessageCreateService, MessageUpdateService, MessageDeleteService
from ..Services.reaction_service import ReactionListService, ReactionCreateService, ReactionUpdateService, ReactionDeleteService
from ..Services.comment_service import CommentListService, CommentCreateService, CommentUpdateService, CommentDeleteService

def load_routes(api):
    # Servicio de login
    api.add_resource(LoginService, '/security/login')
    api.add_resource(UserService, '/security/user-id')

    # Servicios CRUD para usuarios
    api.add_resource(UserListService, '/user/list')
    api.add_resource(UserCreateService, '/user/create')
    api.add_resource(UserUpdateService, '/user/update/<int:user_id>')
    api.add_resource(UserDeleteService, '/user/delete/<int:user_id>')
    api.add_resource(UserDetailsService, '/user/details/<int:user_id>')
    api.add_resource(UserPostsService, '/user/posts/<int:user_id>')

    # Servicios CRUD para publicaciones
    api.add_resource(PostListService, '/post/list')
    api.add_resource(PostCreateService, '/post/create')
    api.add_resource(PostUpdateService, '/post/update/<int:post_id>')
    api.add_resource(PostDeleteService, '/post/delete/<int:post_id>')

    # Servicios CRUD para historias
    api.add_resource(StoryListService, '/story/list')
    api.add_resource(StoryCreateService, '/story/create')
    api.add_resource(StoryUpdateService, '/story/update/<int:story_id>')
    api.add_resource(StoryDeleteService, '/story/delete/<int:story_id>')

    # Servicios CRUD para solicitudes de amistad
    api.add_resource(FriendRequestListService, '/friendrequest/list')
    api.add_resource(FriendRequestCreateService, '/friendrequest/create')
    api.add_resource(FriendRequestUpdateService, '/friendrequest/update/<int:request_id>')
    api.add_resource(FriendRequestDeleteService, '/friendrequest/delete/<int:request_id>')

    # Servicios CRUD para amigos
    api.add_resource(AmigosListService, '/amigos/list')
    api.add_resource(AmigosCreateService, '/amigos/create')
    api.add_resource(AmigosDeleteService, '/amigos/delete/<int:amigo_id>')

    # Servicios CRUD para mensajes
    api.add_resource(MessageListService, '/message/list')
    api.add_resource(MessageDetailService, '/message/list/<int:remitente_id>/<int:destinatario_id>')
    api.add_resource(MessageCreateService, '/message/create')
    api.add_resource(MessageUpdateService, '/message/update/<int:message_id>')
    api.add_resource(MessageDeleteService, '/message/delete/<int:message_id>')

    # Servicios CRUD para reacciones
    api.add_resource(ReactionListService, '/reaction/list')
    api.add_resource(ReactionCreateService, '/reaction/create')
    api.add_resource(ReactionUpdateService, '/reaction/update/<int:reaction_id>')
    api.add_resource(ReactionDeleteService, '/reaction/delete/<int:reaction_id>')

    # Servicios CRUD para comentarios
    api.add_resource(CommentListService, '/comment/list')
    api.add_resource(CommentCreateService, '/comment/create')
    api.add_resource(CommentUpdateService, '/comment/update/<int:comment_id>')
    api.add_resource(CommentDeleteService, '/comment/delete/<int:comment_id>')






