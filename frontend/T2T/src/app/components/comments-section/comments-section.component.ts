import { Component, Input } from '@angular/core';
import { Comment } from '../../model/Comment';
import { CommonModule, DatePipe } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'comments-section',
  standalone: true,
  imports: [DatePipe, FormsModule, CommonModule],
  templateUrl: './comments-section.component.html',
  styleUrl: './comments-section.component.scss'
})
export class CommentsSectionComponent {
  @Input() comments!: Comment[];
  desc: string;

  constructor() {
    this.desc = "";
  }

  addComment() {
    // cal API
    this.desc = "";
  }

  addChildComment(id: number) {
    // call API
    this.desc = "";
  }

}
