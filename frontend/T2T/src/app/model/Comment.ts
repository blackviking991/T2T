export interface Comment {
    id: number;
    desc: string;
    likes: number;
    postId: number;
    createdBy: string;
    createdTime: Date;
    parentComments: number[];
    childComments: number[];
}