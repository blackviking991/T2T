import { ApplicationConfig } from '@angular/core';
import { provideRouter } from '@angular/router';
import { EditorModule, TINYMCE_SCRIPT_SRC  } from '@tinymce/tinymce-angular'
import { routes } from './app.routes';
import { provideClientHydration } from '@angular/platform-browser';
import { provideAnimations } from '@angular/platform-browser/animations';

export const appConfig: ApplicationConfig = {
  providers: [provideRouter(routes), provideClientHydration(), provideAnimations(), provideAnimations(), { provide: TINYMCE_SCRIPT_SRC, useValue: 'tinymce/tinymce.min.js' }]
};
