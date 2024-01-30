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
export class ViewPostComponent implements OnInit{
  editorConfig = {
    base_url: '/tinymce',
    suffix: '.min',
    menubar: false,
    toolbar: false,
    skin: "oxide-dark", 
    content_css: "dark",
    plugins: '',
    height: 650,
  };
  route: ActivatedRoute = inject(ActivatedRoute);
  postId!: string; 
  post!: Post;
  isLiked!: boolean;

  constructor(private http: HttpClient) {};

  ngOnInit(): void {
    this.postId = this.route.snapshot.params['id'];
    // fetch post by ID
    this.http.get("http://localhost:8080/posts/get/" + this.postId, {
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${localStorage.getItem("access_token")}`
      }
    }).subscribe((res: any) => {
      this.post = res.post;
      this.isLiked = res.post.isLiked;
    }, (err => {
      console.log("Error fetching post details for id " + this.postId);
    }));
  }

  toggleLikes() {
    // update like
    this.http.post(`http://localhost:8080/posts/like/${this.postId}/${this.isLiked ? 1 : 0}`, {
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${localStorage.getItem("access_token")}`
      }
    }).subscribe((res: any) => {
      console.log(res);
      this.post = { ...this.post };
    }, (err => {
      console.log("Error fetching post details for id " + this.postId);
    }));
  }
}
