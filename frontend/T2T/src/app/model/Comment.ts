export interface Comment {
    id: number;
    desc: string;
    likes: number;
    postId: number;
    createdBy: string;
    createdAt: Date;
    parentComments: number[];
    childComments: number[];
    comments: Comment[];
}