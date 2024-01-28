import { Component, Input } from '@angular/core';
import { Post } from '../../model/Post';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'post-preview',
  templateUrl: './post-preview.component.html',
  styleUrl: './post-preview.component.scss',
  standalone: true,
  imports: [RouterModule, CommonModule]
})
export class PostPreviewComponent {
  @Input() posts!: Post[];

  formatDesc(desc: string) {
    return desc.length > 30
      ? desc.substring(0, 30) + "..."
      : desc;
  }

  toggleLikes() {
    // call API to like
  }
}
