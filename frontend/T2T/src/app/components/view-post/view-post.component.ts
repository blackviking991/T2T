import { Component, inject } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Comment } from '../../model/Comment';
import { CommentsSectionComponent } from '../comments-section/comments-section.component';

@Component({
  selector: 'app-view-post',
  standalone: true,
  imports: [CommentsSectionComponent],
  templateUrl: './view-post.component.html',
  styleUrl: './view-post.component.scss'
})
export class ViewPostComponent {

  route: ActivatedRoute = inject(ActivatedRoute);
  postId: number; 
  comments: Comment[];

  constructor() {
    this.postId = Number(this.route.snapshot.params['id']);
    // dummy data, make API call
    let comment: Comment = {
      id: 1,
      desc: "Take me home!Take me home!Take me home!Take me home!Take me home!Take me home!Take me home!Take me home!Take me home!Take me home!Take me home!Take me home!",
      likes: 5,
      postId: 3,
      createdBy: "Test User",
      createdAt: new Date(),
      parentComments: [1, 2, 3],
      childComments: [1, 2, 3],
      comments: []
    }
    comment.comments = [comment, { ...comment, id: 2}, { ...comment, id: 3}];
    this.comments = [comment, { ...comment, id: 2}, { ...comment, id: 3}];
  }

}
