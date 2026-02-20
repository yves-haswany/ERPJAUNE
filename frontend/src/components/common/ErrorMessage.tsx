interface Props {
  message: string;
}

export default function ErrorMessage({ message }: Props) {
  return (
    <div className="bg-red-100 text-red-600 p-4 rounded">
      {message}
    </div>
  );
}
