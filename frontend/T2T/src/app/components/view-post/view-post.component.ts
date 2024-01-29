import { Component, OnInit, inject } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import {MatIconModule} from '@angular/material/icon';
import { EditorModule } from '@tinymce/tinymce-angular'
import {MatChipsModule} from '@angular/material/chips';
import { Comment } from '../../model/Comment';
import { CommentsSectionComponent } from '../comments-section/comments-section.component';
import { NavbarComponent } from '../navbar/navbar.component';
import { Post } from '../../model/Post';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { DatePipe } from '@angular/common';

@Component({
  selector: 'app-view-post',
  standalone: true,
  imports: [HttpClientModule, DatePipe, MatIconModule, EditorModule, MatChipsModule, NavbarComponent, CommentsSectionComponent],
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
  route: ActivatedRoute = inject(ActivatedRoute);
  postId: string; 
  post!: Post;

  constructor(private http: HttpClient) {
    this.postId = this.route.snapshot.params['id'];
    // fetch post by ID
    this.http.get("http://localhost:8080/posts/get/" + this.postId, {
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${localStorage.getItem("access_token")}`
      }
    }).subscribe((res: any) => {
      this.post = res.post;
    }, (err => {
      console.log("Error fetching post details for id " + this.postId);
    }));
  }

}
