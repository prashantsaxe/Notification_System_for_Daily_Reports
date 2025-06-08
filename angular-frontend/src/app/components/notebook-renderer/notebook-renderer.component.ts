import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../services/api.service';
import { Notebook } from '../../models';

@Component({
  selector: 'app-notebook-renderer',
  templateUrl: './notebook-renderer.component.html',
  styleUrls: ['./notebook-renderer.component.css']
})
export class NotebookRendererComponent implements OnInit {
  notebooks: Notebook[] = [];
  loading: boolean = true;

  constructor(private apiService: ApiService) {}

  ngOnInit(): void {
    this.fetchNotebooks();
  }

  fetchNotebooks(): void {
    this.apiService.getNotebooks().subscribe(
      (data: Notebook[]) => {
        this.notebooks = data;
        this.loading = false;
      },
      (error) => {
        console.error('Error fetching notebooks', error);
        this.loading = false;
      }
    );
  }

  saveNotebook(notebook: Notebook): void {
    this.apiService.saveNotebook(notebook).subscribe(
      () => {
        console.log('Notebook saved successfully');
      },
      (error) => {
        console.error('Error saving notebook', error);
      }
    );
  }
}