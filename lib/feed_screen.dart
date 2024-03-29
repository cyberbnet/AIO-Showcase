import 'dart:async';

import 'package:flutter/cupertino.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:flutter/painting.dart';
import 'package:flutter_food_delivery_app/repository.dart';
import 'package:flutter_food_delivery_app/screens/General/item_widget_screen.dart';

import 'colors.dart';
import 'language.dart';
import 'models/Article_Model/article_model.dart';
import 'models/User_Model/user_model.dart';

class Tagstatekeys {
  static final _tagStateKey1 = const Key('__TSK1__');
}

class ClipsScreen extends StatefulWidget {
  final User user;
  const ClipsScreen({Key key, this.user}) : super(key: key);

  @override
  ClipsScreenState createState() => ClipsScreenState(user: user);
}

class ClipsScreenState extends State<ClipsScreen> {
  final User user;
  ClipsScreenState({Key key, this.user});
  int page = 1;
  List<Article> articles = [];
  Future fetchPostsfuture;
  bool isLoading = false;
  bool details;
  bool lol;
  @override
  Future<User> callUser(String userid) async {
    Future<User> _user = FetchUser(userid);
    return _user;
  }

  @override
  void initState() {
    fetchPostsfuture =
        FetchFollowedArticlesAll(user.id, page, user, false, '', '', '');
  }

  void initstats(Article article) {
    isarticleliked(user.id, article.id)
      ..then((result) {
        article.likeresult = result;
      });
    isarticledisliked(user.id, article.id)
      ..then((result) {
        article.dislikeresult = result;
      });
    isarticlebookmarked(user.id, article.id)
      ..then((result) {
        article.bookmarkresult = result;
      });
    articlebookmarkid(user.id, article.id)
      ..then((result) {
        article.bookmarkidresult = result;
      });
  }

  Future _loadData() async {
    FetchFollowedArticlesAll(user.id, page, user, false, '', '', '')
      ..then((result) {
        setState(() {
          for (final item in result) articles.add(item);
          isLoading = false;
          return;
        });
      });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: colordtmainone,
      body: FutureBuilder<List<Article>>(
        future: fetchPostsfuture,
        builder: (context, snapshot) {
          if (snapshot.hasError) print(snapshot.error);
          articles = snapshot.data;
          return snapshot.hasData
              ? (snapshot.data.length == 0
                  ? Center(
                      child: Text(nopostst,
                          style: TextStyle(
                              color: colordtmaintwo,
                              fontWeight: FontWeight.bold)),
                    )
                  : PageView.builder(
                      onPageChanged: (indexpage) {
                        if (indexpage + 1 == articles.length) {
                          page = page + 1;
                          _loadData();
                        }
                      },
                      scrollDirection: Axis.vertical,
                      physics: ClampingScrollPhysics(),
                      itemBuilder: (context, index) {
                        return ArticleWidgetScreen(
                          user: user,
                          post: articles[index],
                          ischosing: false,
                        );
                      },
                      itemCount: articles.length))
              : Center(
                  child: CircularProgressIndicator(
                      backgroundColor: Colors.pink,
                      valueColor: new AlwaysStoppedAnimation<Color>(
                          Colors.pinkAccent)));
        },
      ),
    );
  }
}
