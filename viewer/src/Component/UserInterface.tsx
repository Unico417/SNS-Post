import React from "react";
import Style from "./user-interface.scss";

type Props = {};
type State = {
};

export default class UserInterface extends React.Component<Props, State>{
    text: string;
    targetFile?: File;
    imageViewerRef: React.RefObject<HTMLDivElement>;

    constructor(props: Props) {
        super(props);

        this.text = '';
        this.targetFile = undefined;
        this.imageViewerRef = React.createRef();

        this.state = {
        };
    }

    dropFile(e: React.DragEvent<HTMLInputElement>) {
        const file = e.nativeEvent.dataTransfer?.files[0];
        if (!file) return;
        this.targetFile = file;

        const fileReader = new FileReader();
        fileReader.readAsDataURL(file);
        let loadFileURL = '';
        fileReader.addEventListener('load', () => {
            const url = fileReader.result as string;
            if (!url)
                return;
            const imageNode = document.createElement('img');
            imageNode.src = url;

            const imageViewer = this.imageViewerRef.current as HTMLDivElement;
            imageViewer.innerHTML = '';
            imageViewer.appendChild(imageNode);
        });
    }

    onSubmit(e: React.PointerEvent<HTMLDivElement>) {

        if (!this.text && !this.targetFile)
            return;

        const formData = new FormData();
        if (this.targetFile) {
            formData.append('image', this.targetFile);
        }
        formData.append('text', this.text);

        fetch('http://localhost:22222/post', {
            method: 'POST',
            body: formData,
        });
    }

    render(): React.ReactNode {
        return (
            <div id={Style['post-form']}>
                <div className={Style.up}>
                    <div className={Style.left}>
                        <textarea
                            name="post-content"
                            id={Style['post-content']}
                            defaultValue={''}
                            onChange={(e) => { this.text = e.target.value.trim(); }} />
                    </div>
                    <div className={Style.right}>
                        <div
                            className={Style['image-preview']}
                            ref={this.imageViewerRef}
                        >
                            <span>画像をドロップ</span>
                        </div>
                        <input
                            className={Style['image-reciever']}
                            id='image-input'
                            type="file"
                            onDrop={this.dropFile.bind(this)} />
                    </div>
                </div>
                <div className={Style.down}>

                </div>
                <div
                    className={Style.submit}
                    onClick={this.onSubmit.bind(this)}></div>
            </div >
        );
    }
}
