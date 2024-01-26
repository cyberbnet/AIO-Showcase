from accounts.views import UserMessageCountViewSet,BoughtCheckViewSet,RequestItemViewSet,RequestItemChoiceViewSet,CartItemViewSet,CartItemChoiceViewSet,UserMessageImageViewSet,UserMessageVideoViewSet,ArticleChoiceCategoryViewSet,ArticleChoiceViewSet,UserGetMessageViewSet,PublicUserViewSet,TagUsersViewSet,FetchSubuserNotificationViewSet,FollowedArticleCategoryViewSet,PublicArticleCategoryViewSet,PublicArticleCategoryViewSet,FollowedArticleCategoryViewSet,FetchSubUserViewSet,FollowedUserLocationViewSet,FollowedUserMailViewSet,FollowedUserPhoneViewSet,FollowedCalendarTimeViewSet,PublicCalendarTimeViewSet,SubuserCommentViewSet,ArticleUnLikeViewSet,RegisteringUserViewSet,ArticleUnDislikeViewSet,UserUnDislikeViewSet,ArticleUnDislikeViewSet,ArticleUnDislikeViewSet,ArticleUnDislikeViewSet,ArticleUnDislikeViewSet,ArticleUnLikeViewSet,ArticleUnLikeViewSet,UserUnLikeViewSet,ArticleUnLikeViewSet,ArticleUnLikeViewSet,ArticleSubuserTaggedViewSet,ArticleLikeViewSet,ArticleLikeViewSet,ArticleLikeViewSet,ArticleLikeViewSet,ArticleDislikeViewSet,ArticleDislikeViewSet,ArticleDislikeViewSet,ArticleDislikeViewSet,UserDislikeViewSet,ArticleDislikeViewSet,SubuserArticleLikeViewSet,ArticleUserTaggedViewSet,SubuserArticleCommentViewSet,SubuserRequestViewSet,SubuserArticleViewSet,SubuserArticleViewSet,SubuserArticleViewSet,SubuserArticleViewSet,SubuserArticleViewSet,SubuserArticleCommentViewSet,SubuserArticleCommentViewSet,SubuserArticleCommentViewSet,SubuserArticleCommentViewSet,ArticleCommentViewSet,RequestImageViewSet,RequestCheckBoxViewSet,RequestFormViewSet,ArticleFormViewSet,ArticleCheckboxViewSet,PublicArticleViewSet,ArticleImageViewSet,ArticleViewSet,ArticleTagViewSet,ArticleCategoryViewSet,PublicArticleViewSet,ArticleTagViewSet,ArticleCommentViewSet,ArticleCommentViewSet,ArticleCommentViewSet,ArticleTagViewSet,ArticleTagViewSet,UserViewViewSet,ArticleImageViewSet,ArticleViewSet,ArticleCategoryViewSet,PublicArticleofGroupsViewSet,PublicArticlePriceViewSet,NonGrouppArticleViewSet,PrivateUserViewSet,RegisterUserCheckViewSet,ArticleCreateViewSet,ArticleImageViewSet,ArticleSharedImageViewSet,ArticleBookmarkViewSet,ArticleVideoViewSet,ArticleTagViewSet,ArticleViewViewSet,ArticleLikeViewSet,ArticleUserTagViewSet,ArticleCommentViewSet,RequestViewSet,ArticleViewSet,CalendarDateViewSet,CalendarScheduleViewSet,UserReportViewSet,UserMessageViewSet,UserBlockViewSet,UserTagViewSet,UserCommentViewSet,UserFollowViewSet,UserLikeViewSet,UserImageViewSet,UserPhoneViewSet,UserMailViewSet,UserLocationViewSet,ArticleSharedVideoViewSet,CalendarTimeViewSet,CalendarStatusViewSet,ArticleViewSet,ArticleImageViewSet,ArticleImageViewSet,PublicArticleViewSet,FetchUserViewSet,UserViewSet,UsersViewSet,SubUserViewSet,UserArticleViewSet,RegisterUserViewSet,AllUnauthUserViewSet,FollowedUserFollowingViewSet,PublicUserFollowedViewSet,FollowedUserFollowedViewSet,FollowedUserFollowingViewSet,PublicUserFollowingViewSet,UserFollowingViewSet,UserFollowedViewSet,PublicArticleCommentViewSet,PublicUserCommentViewSet,PublicArticleCommentViewSet,PublicArticleCommentViewSet,PublicArticleCommentViewSet,PublicArticleCommentViewSet,FollowedArticleCommentViewSet,FollowedUserCommentViewSet,FollowedArticleCommentViewSet,FollowedArticleCommentViewSet,FollowedArticleCommentViewSet,FollowedArticleCommentViewSet,PublicUserMailViewSet,PublicUserPhoneViewSet,PublicUserLocationViewSet,UserCommentLikeViewSet,ArticleCommentLikeViewSet,ArticleCommentLikeViewSet,ArticleCommentLikeViewSet,ArticleCommentLikeViewSet,ArticleCommentLikeViewSet,UserCommentDislikeViewSet,ArticleCommentDislikeViewSet,ArticleCommentDislikeViewSet,ArticleCommentDislikeViewSet,ArticleCommentDislikeViewSet,ArticleCommentDislikeViewSet,UserCommentUnLikeViewSet,ArticleCommentUnLikeViewSet,ArticleCommentUnLikeViewSet,ArticleCommentUnLikeViewSet,ArticleCommentUnLikeViewSet,ArticleCommentUnLikeViewSet,UserCommentUnDislikeViewSet,ArticleCommentUnDislikeViewSet,ArticleCommentUnDislikeViewSet,ArticleCommentUnDislikeViewSet,ArticleCommentUnDislikeViewSet,PublicArticleFIOViewSet,PublicArticleFIOViewSet,PublicArticleFIOViewSet,PublicArticleFIOViewSet,PublicArticleFIOViewSet,FollowedArticleFIOViewSet,FollowedArticleFIOViewSet,FollowedArticleFIOViewSet,FollowedArticleFIOViewSet,FollowedArticleFIOViewSet,PublicArticleFIOViewSet,FollowedArticleFIOViewSet,ArticleCommentUnDislikeViewSet,ArticleCommentUnLikeViewSet,ArticleCommentDislikeViewSet,ArticleCommentLikeViewSet,FollowedArticleCommentViewSet,PublicArticleCommentViewSet,ArticleUnDislikeViewSet,ArticleUnLikeViewSet,SubuserArticleViewSet,SubuserArticleCommentViewSet,PublicArticleViewSet,ArticleTagViewSet,ArticleViewSet,ArticleCommentViewSet,ArticleImageViewSet,ArticleDislikeViewSet,ArticleLikeViewSet,ArticleChoiceViewSet,ArticleChoiceCategoryViewSet,ArticleCategoryViewSet,FollowedArticleCategoryViewSet,PublicArticleCategoryViewSet,ArticleCheckboxViewSet,PublicArticleCategorySearchViewSet,FollowedArticleCategorySearchViewSet,ArticleFormViewSet,PublicReservationDeactivationMonthViewSet,FollowedReservationDeactivationMonthViewSet,ReservationDeactivationMonthViewSet,ReservationScheduleViewSet,UserCartItemViewSet,ArticleActivityViewSet,ArticleHighlightViewSet,ArticleTravelLocationViewSet,BusinessTypeViewSet,ArticleAmenityViewSet,ArticleDetailCategoryViewSet,ArticleDetailIncludedViewSet,ArticleDetailRuleViewSet,ArticleDetailSpecViewSet,ItemTypeViewSet,UserOpeningHourViewSet,BoughtItemChoiceViewSet,MeetingStatusViewSet,MeetingScheduleViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'articleactivities', ArticleActivityViewSet)
router.register(r'articlehighlights', ArticleHighlightViewSet)
router.register(r'articleamenities', ArticleAmenityViewSet)
router.register(r'boughtchecks', BoughtCheckViewSet)
router.register(r'boughtitemchoices', BoughtItemChoiceViewSet)
router.register(r'articletravellocations', ArticleTravelLocationViewSet)
router.register(r'articledetailcategories', ArticleDetailCategoryViewSet)
router.register(r'articledetailincludeds', ArticleDetailIncludedViewSet)
router.register(r'articledetailrules', ArticleDetailRuleViewSet)
router.register(r'useropeninghours', UserOpeningHourViewSet)
router.register(r'articledetailspecs', ArticleDetailSpecViewSet)
router.register(r'searchfollowedarticlecategories',FollowedArticleCategorySearchViewSet)
router.register(r'meetingschedules', MeetingScheduleViewSet)
router.register(r'meetingstatuses', MeetingStatusViewSet)
router.register(r'searchpublicarticlecategories',PublicArticleCategorySearchViewSet)
router.register(r'articlechoices', ArticleChoiceViewSet)
router.register(r'articlechoicecategories', ArticleChoiceCategoryViewSet)
router.register(r'articleforms', ArticleFormViewSet)
router.register(r'usercartitems', UserCartItemViewSet)
router.register(r'articlecheckboxes', ArticleCheckboxViewSet)
router.register(r'articlecategories', ArticleCategoryViewSet)
router.register(r'publicarticlecategories', PublicArticleCategoryViewSet)
router.register(r'followedarticlecategories', FollowedArticleCategoryViewSet)
router.register(r'reservationschedules', ReservationScheduleViewSet)
router.register(r'publicreservationdeactivationmonths', PublicReservationDeactivationMonthViewSet)
router.register(r'followedreservationdeactivationmonths', FollowedReservationDeactivationMonthViewSet)
router.register(r'reservationdeactivationmonths', ReservationDeactivationMonthViewSet)
router.register(r'userreports', UserReportViewSet)
router.register(r'userfollowings', UserFollowingViewSet)
router.register(r'userfolloweds', UserFollowedViewSet)
router.register(r'usermessages', UserMessageViewSet)
router.register(r'usermessagecount', UserMessageCountViewSet)
router.register(r'usergetmessages',UserGetMessageViewSet)
router.register(r'userblocks', UserBlockViewSet)
router.register(r'fetchsubusers', FetchSubUserViewSet)
router.register(r'fetchsubusernotifications',FetchSubuserNotificationViewSet)
router.register(r'usertags', UserTagViewSet)
router.register(r'requestitems', RequestItemViewSet)
router.register(r'requestitemchoices', RequestItemChoiceViewSet)
router.register(r'cartitems', CartItemViewSet)
router.register(r'cartitemchoices', CartItemChoiceViewSet)
router.register(r'usermessageimages', UserMessageImageViewSet)
router.register(r'usermessagevideos', UserMessageVideoViewSet)
router.register(r'tagusers',TagUsersViewSet)
router.register(r'ownuser', UserViewSet)
router.register(r'publicuserphones', PublicUserPhoneViewSet)
router.register(r'publicusermails', PublicUserMailViewSet)
router.register(r'publicuserlocations', PublicUserLocationViewSet)
router.register(r'unusers', AllUnauthUserViewSet)
router.register(r'publicusers', PublicUserViewSet)
router.register(r'privateusers', PrivateUserViewSet)
router.register(r'publicfollowings', PublicUserFollowedViewSet)
router.register(r'followedfollowings', FollowedUserFollowedViewSet)
router.register(r'publicfolloweds', FollowedUserFollowingViewSet)
router.register(r'followedfolloweds', PublicUserFollowingViewSet)
router.register(r'articles', NonGrouppArticleViewSet)
router.register(r'registeringcheck', RegisteringUserViewSet)
router.register(r'registeredusers', RegisterUserCheckViewSet)
router.register(r'register', RegisterUserViewSet)
router.register(r'userss', UsersViewSet)
router.register(r'publicuserfollows', PublicUserFollowingViewSet)
router.register(r'followeduserfollows', FollowedUserFollowingViewSet)
router.register(r'subusertaggedarticles', ArticleSubuserTaggedViewSet)
router.register(r'usertaggedarticles', ArticleUserTaggedViewSet)
router.register(r'requestcheckboxes', RequestCheckBoxViewSet)
router.register(r'requestforms', RequestFormViewSet)
router.register(r'requestimages', RequestImageViewSet)
router.register(r'subusers', SubUserViewSet)
router.register(r'followedusers', FetchUserViewSet)
router.register(r'userdislikes', UserDislikeViewSet)
router.register(r'articledislikes', ArticleDislikeViewSet)
router.register(r'userimages', UserImageViewSet)
router.register(r'userphones', UserPhoneViewSet)
router.register(r'usermails', UserMailViewSet)
router.register(r'userviews', UserViewViewSet)
router.register(r'userlocations', UserLocationViewSet)
router.register(r'usercomments', UserCommentViewSet)
router.register(r'userfollows', UserFollowViewSet)
router.register(r'requests', RequestViewSet)
router.register(r'userlikes', UserLikeViewSet)
router.register(r'fetcharticles', UserArticleViewSet)
router.register(r'publicarticles',PublicArticleViewSet)
router.register(r'publicarticleofgroups',PublicArticleofGroupsViewSet)
router.register(r'publicarticlesbyprice',PublicArticlePriceViewSet)
router.register(r'articlecreate', ArticleCreateViewSet)
router.register(r'articleimages', ArticleImageViewSet)
router.register(r'articlesharedimages', ArticleSharedImageViewSet)
router.register(r'articlesharedvideos', ArticleSharedVideoViewSet)
router.register(r'articlebookmarks', ArticleBookmarkViewSet)
router.register(r'articlevideos', ArticleVideoViewSet)
router.register(r'articletags', ArticleTagViewSet)
router.register(r'articleviews', ArticleViewViewSet)
router.register(r'publicusercomments', PublicUserCommentViewSet)
router.register(r'publicarticlecomments', PublicArticleCommentViewSet)
router.register(r'followedusercomments', FollowedUserCommentViewSet)
router.register(r'followedarticlecomments', FollowedArticleCommentViewSet)
router.register(r'articlelikes', ArticleLikeViewSet)
router.register(r'articleusertags', ArticleUserTagViewSet)
router.register(r'articlecomments', ArticleCommentViewSet)
router.register(r'calendarstatuses', CalendarStatusViewSet)
router.register(r'calendartimes', CalendarTimeViewSet)
router.register(r'calendardates', CalendarDateViewSet)
router.register(r'calendarschedules', CalendarScheduleViewSet)
router.register(r'subuserrequests', SubuserRequestViewSet)
router.register(r'subuserarticlelikes', SubuserArticleLikeViewSet)
router.register(r'subuserarticlecomments', SubuserArticleCommentViewSet)
router.register(r'subuserarticles', SubuserArticleViewSet)
router.register(r'articleunlikes', ArticleUnLikeViewSet)
router.register(r'userundislikes', UserUnDislikeViewSet)
router.register(r'articleundislikes', ArticleUnDislikeViewSet)
router.register(r'subusercomments', SubuserCommentViewSet)
router.register(r'publiccalendartimes', PublicCalendarTimeViewSet)
router.register(r'followeduserlocations', FollowedUserLocationViewSet)
router.register(r'followeduserphones', FollowedUserPhoneViewSet)
router.register(r'followedusermails', FollowedUserMailViewSet)
router.register(r'followedcalendartimes', FollowedCalendarTimeViewSet)
router.register(r'userunlikes', UserUnLikeViewSet)
router.register(r'usercommentlikes',UserCommentLikeViewSet)
router.register(r'articlecommentlikes',ArticleCommentLikeViewSet)
router.register(r'usercommentdislikes',UserCommentDislikeViewSet)
router.register(r'articlecommentdislikes',ArticleCommentDislikeViewSet)
router.register(r'usercommentunlikes',UserCommentUnLikeViewSet)
router.register(r'articlecommentunlikes',ArticleCommentUnLikeViewSet)
router.register(r'usercommentundislikes',UserCommentUnDislikeViewSet)
router.register(r'articlecommentundislikes',ArticleCommentUnDislikeViewSet)
router.register(r'publicarticleFIO', PublicArticleFIOViewSet)
router.register(r'followedarticleFIO', FollowedArticleFIOViewSet)


urlpatterns = router.urls


