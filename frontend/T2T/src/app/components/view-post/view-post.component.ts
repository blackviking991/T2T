import { Component, inject } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-view-post',
  standalone: true,
  imports: [],
  templateUrl: './view-post.component.html',
  styleUrl: './view-post.component.scss'
})
export class ViewPostComponent {

  route: ActivatedRoute = inject(ActivatedRoute);
  postId: number; 

  constructor() {
    this.postId = Number(this.route.snapshot.params['id']);
  }

}
