import { Component, inject } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-forum-page',
  standalone: true,
  imports: [],
  templateUrl: './forum-page.component.html',
  styleUrl: './forum-page.component.scss'
})
export class ForumPageComponent {

  route: ActivatedRoute = inject(ActivatedRoute);
  forumName: String;

  constructor() {
    this.forumName = this.route.snapshot.params['name'];
  }

}
