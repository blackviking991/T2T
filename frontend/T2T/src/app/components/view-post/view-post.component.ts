import { Component, OnInit, inject } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import {MatIconModule} from '@angular/material/icon';
import { EditorModule } from '@tinymce/tinymce-angular'
import {MatChipsModule} from '@angular/material/chips';
import { Comment } from '../../model/Comment';
import { CommentsSectionComponent } from '../comments-section/comments-section.component';
import { NavbarComponent } from '../navbar/navbar.component';
import { Post } from '../../model/Post';

@Component({
  selector: 'app-view-post',
  standalone: true,
  imports: [MatIconModule, EditorModule, MatChipsModule,NavbarComponent, CommentsSectionComponent],
  templateUrl: './view-post.component.html',
  styleUrl: './view-post.component.scss'
})
export class ViewPostComponent {
  editorConfig = {
    base_url: '/tinymce',
    suffix: '.min',
    menubar: false,
    toolbar: false,
    plugins: '',
    height: 650,
  };
  tags = ['frontend', 'Angular', 'Dev'];
  initialVal = '<h1><img style=\"display: block; margin-left: auto; margin-right: auto;\" src=\"https://miro.medium.com/v2/resize:fit:1400/format:webp/1*1HXCJCOpzKdmQI33ZrEIlg.png\" alt=\"\" width=\"716\" height=\"224\">Angular 17</h1>\n<p><span style=\"font-family: helvetica, arial, sans-serif;\">Angular version 17 released on November 8, 2023 and the hype is real! There are so many things to talk about and get your head around to create modern web apps and updating your existing Angular apps. You can read about the details of each of the new changes on the&nbsp;<a class=\"af nx\" href=\"https://goo.gle/angular-dot-dev\" target=\"_blank\" rel=\"noopener ugc nofollow\">Angular blog post</a>, but lets talk about why these changes are important to you as an Angular developer.</span></p>\n<h2><span style=\"font-family: helvetica, arial, sans-serif;\">New features</span></h2>\n<p id=\"170e\" class=\"pw-post-body-paragraph mz na gr nb b nc nd ne nf ng nh ni nj nk nl nm nn no np nq nr ns nt nu nv nw gk bj\" data-selectable-paragraph=\"\">Before diving in, lets take a look at all the new things in v17&hellip;</p>\n<ul class=\"\">\n<li id=\"0f1d\" class=\"mz na gr nb b nc nd ne nf ng nh ni nj nk nl nm nn no np nq nr ns nt nu nv nw ny nz oa bj\" data-selectable-paragraph=\"\">logo redesign</li>\n<li id=\"c23a\" class=\"mz na gr nb b nc ob ne nf ng oc ni nj nk od nm nn no oe nq nr ns of nu nv nw ny nz oa bj\" data-selectable-paragraph=\"\">website moving from&nbsp;<a class=\"af nx\" href=\"https://angular.io/\" target=\"_blank\" rel=\"noopener ugc nofollow\">angular.io</a>&nbsp;to&nbsp;<a class=\"af nx\" href=\"https://angular.dev/\" target=\"_blank\" rel=\"noopener ugc nofollow\">angular.dev</a></li>\n<li id=\"fa54\" class=\"mz na gr nb b nc ob ne nf ng oc ni nj nk od nm nn no oe nq nr ns of nu nv nw ny nz oa bj\" data-selectable-paragraph=\"\">standalone applications are now the default for new applications</li>\n<li id=\"b63d\" class=\"mz na gr nb b nc ob ne nf ng oc ni nj nk od nm nn no oe nq nr ns of nu nv nw ny nz oa bj\" data-selectable-paragraph=\"\">signals are out of dev preview and are now stable</li>\n<li id=\"8563\" class=\"mz na gr nb b nc ob ne nf ng oc ni nj nk od nm nn no oe nq nr ns of nu nv nw ny nz oa bj\" data-selectable-paragraph=\"\">server-side rendering improvements</li>\n<li id=\"e34e\" class=\"mz na gr nb b nc ob ne nf ng oc ni nj nk od nm nn no oe nq nr ns of nu nv nw ny nz oa bj\" data-selectable-paragraph=\"\">hydration is out of dev preview and is now stable</li>\n<li id=\"a8b0\" class=\"mz na gr nb b nc ob ne nf ng oc ni nj nk od nm nn no oe nq nr ns of nu nv nw ny nz oa bj\" data-selectable-paragraph=\"\">control flow (<code class=\"cw og oh oi oj b\">@if</code>,&nbsp;<code class=\"cw og oh oi oj b\">@for</code>,&nbsp;<code class=\"cw og oh oi oj b\">@switch</code>) *developer preview</li>\n<li id=\"9732\" class=\"mz na gr nb b nc ob ne nf ng oc ni nj nk od nm nn no oe nq nr ns of nu nv nw ny nz oa bj\" data-selectable-paragraph=\"\">defer&nbsp;<em class=\"ok\">(just going to leave this here because justice can not be paid this briefly)</em> *developer preview</li>\n</ul>"';
  route: ActivatedRoute = inject(ActivatedRoute);
  postId: number; 
  post: Post;
  comments: Comment[];

  constructor() {
    this.postId = Number(this.route.snapshot.params['id']);
    // dummy data, make API call
    this.post = {
      pID: "1",
      title: "Title",
      desc: "DescpDescpDescpDescpDescpDescpDescpDescpDescpDescpDescpDescpDescpDescpDescpDescpDescpDescpDescpDescpDescpDescpDescpDescpDescpDescpDescpDescpDescpDescpDescpDescpDescpDescpDescpDescp",
      shortDesc: "Short Desc",
      createdBy: "Test User",
      createdTime: new Date(),
      tags: ["tag1", "tag1", "tagsdfadfs"],
      likes: 5,
      forumName: "8",
      views: 50
    }
    let comment: Comment = {
      cID: "1",
      text: "Take me home!Take me home!Take me home!Take me home!Take me home!Take me home!Take me home!Take me home!Take me home!Take me home!Take me home!Take me home!",
      likes: 5,
      postId: 3,
      createdBy: "Test User",
      createdTime: new Date()
    }
    comment.childComments = [comment, { ...comment, cID: "2"}, { ...comment, cID: "3"}];
    this.comments = [comment, { ...comment, cID: "2"}, { ...comment, cID: "3"}];
  }

}
