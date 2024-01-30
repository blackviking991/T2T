import { Component, Input, Output, EventEmitter, OnInit } from '@angular/core';
import {MatButtonModule} from '@angular/material/button';
import {MatCardModule} from '@angular/material/card';
import { ReactiveFormsModule } from '@angular/forms';
import {MatInputModule} from '@angular/material/input';
import {MatFormFieldModule} from '@angular/material/form-field';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { LeaderComponent } from '../leader/leader.component';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { Router } from '@angular/router';
import { MatIcon } from '@angular/material/icon';

@Component({
  selector: 'app-home-page',
  standalone: true,
  imports: [HttpClientModule,MatIcon, MatCardModule,MatButtonModule, ReactiveFormsModule, MatInputModule, MatFormFieldModule, LeaderComponent],
  templateUrl: './home-page.component.html',
  styleUrl: './home-page.component.scss'
})
export class HomePageComponent implements OnInit {
  Loginform: FormGroup = new FormGroup({
    email: new FormControl('', [Validators.required, Validators.email ]),
    password: new FormControl('', [Validators.required]),
  });
  constructor(private http: HttpClient, private router: Router){};
  leaderBoard: any = [];
  ngOnInit(): void {
    this.http.get('http://localhost:8080/users/getLeaders').subscribe((data: any) => {
      console.log(data);
      this.leaderBoard = data;
    },(err => {
      console.log(err);
    }));
  }
  onClick(): void {
    console.log('click')
    const menuToggle = document.querySelector('.toggle');
    const showcase = document.querySelector('.showcase');
    menuToggle!.classList.toggle('active');
    showcase!.classList.toggle('active');
  }

  submit() {
    if (this.Loginform.valid) {
      console.log(this.Loginform.value);
      var body = this.Loginform.value;
      this.http.post('http://localhost:8080/users/login', body).subscribe((res: any) => {
        console.log(res);
        localStorage.setItem('access_token', res.access_token);
        this.router.navigate(['/profile']);
      },(err: any) => {
        console.log(err);
      });
      this.submitEM.emit(this.Loginform.value);
    }
    else{
      this.error = "Invalid details";
       console.log('invalid form');
    }
  }
  @Input() error!: string | null;

  @Output() submitEM = new EventEmitter();
}
