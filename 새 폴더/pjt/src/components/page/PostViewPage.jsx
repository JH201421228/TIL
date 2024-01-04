import React, { useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import styled from "styled-components";
import CommentList from "../list/CommentList";
import TextInput from "../ui/TextInput";
import Button from "../ui/Button";
import data from "../../data.json";

const Wrapper = styled.div`
  padding: 16px;
  width: calc(100% - 32px);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
`;

const Container = styled.div`
  width: 100%;
  max-width: 720px;

  & > * {
    :not(:last-child) {
      margin-bottom: 16px;
    }
  }
`;

const PostContainer = styled.div`
  padding: 8px 16px;
  border: 1px solid grey;
  border-radius: 8px;
`;

const TitleText = styled.p`
  font-size: 28px;
  font-weight: 500;
`;

const ContentText = styled.p`
  font-size: 20px;
  line-height: 32px;
  white-space: pre-wrap;
`;

const CommentLabel = styled.p`
  font-size: 16px;
  font-weight: 500;
`;

const ChatBubble = styled.div`
  background-color: #f0f0f0;
  padding: 10px;
  border-radius: 8px;
  margin-bottom: 10px;
`;

function PostViewPage(props) {
  const navigate = useNavigate();
  const { postId } = useParams();
  const post = data.find((item) => item.id == postId);
  const [comment, setComment] = useState("");

  return (
    <Wrapper>
      <Container>
        <ChatBubble>
          안녕하세요! 이 페이지에서는 포스트를 읽고 댓글을 작성할 수 있어요.
        </ChatBubble>

        <ChatBubble>
          현재 선택한 포스트의 제목은 <strong>{post.title}</strong>이에요.
        </ChatBubble>

        <ChatBubble>
          포스트 내용을 확인해보세요:
          <br />
          <em>{post.content}</em>
        </ChatBubble>

        <CommentLabel>댓글</CommentLabel>
        <CommentList comments={post.comments} />

        <TextInput
          height={40}
          value={comment}
          onChange={(event) => {
            setComment(event.target.value);
          }}
        />
        <Button
          title="댓글 작성하기"
          onClick={() => {
            navigate("/");
          }}
        />
      </Container>
    </Wrapper>
  );
}

export default PostViewPage;
