export interface Notebook {
    id: string;
    title: string;
    cells: Cell[];
}

export interface Cell {
    id: string;
    content: string;
    type: 'markdown' | 'code';
}