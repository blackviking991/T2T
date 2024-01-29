import { Component, Input } from '@angular/core';
import { NavbarComponent } from '../navbar/navbar.component';
import { User } from '../../model/User';
import { Post } from '../../model/Post';
import { PostPreviewComponent } from '../post-preview/post-preview.component';
import { HttpClient, HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-profile-page',
  standalone: true,
  imports: [HttpClientModule, NavbarComponent, PostPreviewComponent],
  templateUrl: './profile-page.component.html',
  styleUrl: './profile-page.component.scss'
})
export class ProfilePageComponent {
  user!: User;
  posts!: Post[];

  constructor(private http: HttpClient) {
    // fetch profile
    this.http.get("http://localhost:8080/users/me", {
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${localStorage.getItem("access_token")}`
      }
    }).subscribe((res: any) => {
      this.user = res.user;
    }, (err => {
      console.log("Error fetching profile details");
    }));

    // fetch user posts
    this.http.get("http://localhost:8080/posts/getUserPosts", {
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${localStorage.getItem("access_token")}`
      }
    }).subscribe((res: any) => {
      this.posts = res.posts;
    }, (err => {
      console.log("Error fetching profile details");
    }));
  }

}
