import { Component, Input, Output, EventEmitter } from '@angular/core';
import {MatButtonModule} from '@angular/material/button';
import {MatCardModule} from '@angular/material/card';
import { ReactiveFormsModule } from '@angular/forms';
import {MatInputModule} from '@angular/material/input';
import {MatFormFieldModule} from '@angular/material/form-field';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { LeaderComponent } from '../leader/leader.component';

@Component({
  selector: 'app-home-page',
  standalone: true,
  imports: [MatCardModule,MatButtonModule, ReactiveFormsModule,MatInputModule, MatFormFieldModule, LeaderComponent],
  templateUrl: './home-page.component.html',
  styleUrl: './home-page.component.scss'
})
export class HomePageComponent {
  Loginform: FormGroup = new FormGroup({
    email: new FormControl('', [Validators.required, Validators.email ]),
    password: new FormControl('', [Validators.required]),
  });

  submit() {
    if (this.Loginform.valid) {
      console.log(this.Loginform.value)
      this.submitEM.emit(this.Loginform.value);
    }
    else{
      this.error = "Invalid details"
    }
  }
  @Input() error!: string | null;

  @Output() submitEM = new EventEmitter();
}
