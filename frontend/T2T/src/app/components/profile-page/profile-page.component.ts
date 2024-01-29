import { Component, Input } from '@angular/core';
import { NavbarComponent } from '../navbar/navbar.component';
import { User } from '../../model/User';
import { Post } from '../../model/Post';
import { PostPreviewComponent } from '../post-preview/post-preview.component';

@Component({
  selector: 'app-profile-page',
  standalone: true,
  imports: [NavbarComponent, PostPreviewComponent],
  templateUrl: './profile-page.component.html',
  styleUrl: './profile-page.component.scss'
})
export class ProfilePageComponent {
  user: User;
  posts: Post[];

  constructor() {
    // dummy data, make API call
    this.user = {
      firstName: "Test",
      lastName: "User",
      email: "test@user.com",
      about: "Testing forums",
      org: ["Test", "User"]
    }
    // dummy data, make API call
    let post: Post = {
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
    this.posts = [post, {...post, desc: "kuygjygk", pID: "2"}, {...post, pID: "3"}];
  }

}
