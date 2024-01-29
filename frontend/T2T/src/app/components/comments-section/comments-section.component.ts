import { Component, Input } from '@angular/core';
import { Comment } from '../../model/Comment';
import { CommonModule, DatePipe } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClient, HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'comments-section',
  standalone: true,
  imports: [HttpClientModule, DatePipe, FormsModule, CommonModule],
  templateUrl: './comments-section.component.html',
  styleUrl: './comments-section.component.scss'
})
export class CommentsSectionComponent {
  @Input() postId!: string;
  @Input() comments!: Comment[];
  
  http: HttpClient;
  desc: string;

  constructor(private httpClient: HttpClient) {
    this.desc = "";
    this.http = httpClient;
  }

  pushComment(body: Comment) {
    this.http.post('http://localhost:8080/comments/add', body, {
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${localStorage.getItem("access_token")}`
      }
    }).subscribe((res: any) => {
      console.log(res);
      if(!this.comments) {
        this.comments = [body];
      } else {
        if(body.parentCommentId) {
          let index = this.comments.findIndex(com => com.cID === body.parentCommentId)
          if(index != -1) {
            let childComments = this.comments[index].childComments ?? [];
            childComments.push(res.comment);
            this.comments[index].childComments = childComments;
          }
        } else {
          this.comments.push(res.comment);
        }
      }
    },(err: any) => {
      console.log(err);
    });
  }

  addComment() {
    // cal API
    this.pushComment({
      text: this.desc,
      postId: this.postId
    });
    this.desc = "";
  }

  addChildComment(cId: string) {
    // call API
    this.pushComment({
      text: this.desc,
      postId: this.postId,
      parentCommentId: cId
    });
    this.desc = "";
  }

}
