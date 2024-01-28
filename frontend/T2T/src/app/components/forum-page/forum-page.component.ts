import { Component, inject } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { PostPreviewComponent } from '../post-preview/post-preview.component';
import { Post } from '../../model/Post';
import { CommonModule } from '@angular/common';
import { NavbarComponent } from '../navbar/navbar.component';

@Component({
  selector: 'app-forum-page',
  standalone: true,
  imports: [PostPreviewComponent, NavbarComponent, CommonModule],
  templateUrl: './forum-page.component.html',
  styleUrl: './forum-page.component.scss'
})
export class ForumPageComponent {

  route: ActivatedRoute = inject(ActivatedRoute);
  forumName: String;
  posts: Post[];

  constructor() {
    this.forumName = this.route.snapshot.params['name'];
    // dummy data, make API call
    let post: Post = {
      id: 1,
      title: "Title",
      desc: "DescpDescpDescpDescpDescpDescpDescpDescpDescpDescpDescpDescpDescpDescpDescpDescpDescpDescpDescpDescpDescpDescpDescpDescpDescpDescpDescpDescpDescpDescpDescpDescpDescpDescpDescpDescp",
      createdBy: "Test User",
      createdAt: new Date(),
      tags: ["tag1", "tag1", "tagsdfadfs"],
      likes: 5,
      commentIds: [1, 2, 3],
      forumTag: 8,
      views: 50
    }
    this.posts = [post, {...post, desc: "kuygjygk", id: 2}, {...post, id: 3}];
  }

}
