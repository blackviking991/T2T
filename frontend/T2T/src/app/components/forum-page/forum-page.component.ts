import { Component, inject } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { PostPreviewComponent } from '../post-preview/post-preview.component';
import { Post } from '../../model/Post';
import { CommonModule } from '@angular/common';
import { NavbarComponent } from '../navbar/navbar.component';
import { HttpClient, HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-forum-page',
  standalone: true,
  imports: [HttpClientModule, PostPreviewComponent, NavbarComponent, CommonModule],
  templateUrl: './forum-page.component.html',
  styleUrl: './forum-page.component.scss'
})
export class ForumPageComponent {

  route: ActivatedRoute = inject(ActivatedRoute);
  forumName: String;
  posts!: Post[];

  constructor(private http: HttpClient) {
    this.forumName = this.route.snapshot.params['name'];
    // fetch posts by forumName
    this.http.get("http://localhost:8080/posts/getForumPosts/" + this.forumName, {
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${localStorage.getItem("access_token")}`
      }
    }).subscribe((res: any) => {
      this.posts = res.posts;
    }, (err => {
      console.log("Error fetching posts for forum " + this.forumName);
    }));
  }

}
