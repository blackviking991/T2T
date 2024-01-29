export interface Comment {
    cID?: string;
    text: string;
    postId: string;
    likes?: number;
    createdBy?: string;
    createdTime?: Date;
    parentCommentId?: string;
    childCommentIds?: string[];
    childComments?: Comment[];
}